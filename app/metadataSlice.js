import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import tinytrader from './apis/tinytrader';


const initialState = {
  data: {},
}

export const fetchMetadata = createAsyncThunk('metadata/fetchMetadata', async () => {
  const response = await tinytrader.get('/metadata/3412/');
  console.log(response.data);
  return response.data;
})

const metadataSlice = createSlice({
  name: 'data',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchMetadata.fulfilled]: (state, action) => {
      state.data = action.payload;
    }
  }
})

export default metadataSlice.reducer;