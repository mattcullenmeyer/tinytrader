import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import tinytrader from '../apis/tinytrader';

const initialState = {
  status: 'idle',
  data: {},
}

export const fetchMetadata = createAsyncThunk(
  'metadata/fetchMetadata', async (ticker_id) => {
    const response = await tinytrader.get(`/metadata/${ticker_id}/`);
    return response.data;
})

const metadataSlice = createSlice({
  name: 'data',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchMetadata.fulfilled]: (state, action) => {
      state.data = action.payload;
      state.status = 'success';
    }
  }
})

export default metadataSlice.reducer;