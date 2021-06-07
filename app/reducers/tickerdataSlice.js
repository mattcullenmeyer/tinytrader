import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import tinytrader from '../apis/tinytrader';

const initialState = {
  status: 'idle',
  data: {}
}

export const fetchTickerdata = createAsyncThunk(
  'ticker/fetchTickerdata', async (ticker) => {
    const response = await tinytrader.get(`/ticker/${ticker}/`);
    return response.data;
})

const tickerdataSlice = createSlice({
  name: 'data',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchTickerdata.fulfilled]: (state, action) => {
      state.data = action.payload;
      state.status = 'success';
    }
  }
})

export default tickerdataSlice.reducer;