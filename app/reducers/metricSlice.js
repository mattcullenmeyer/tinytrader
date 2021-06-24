import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import tinytrader from '../apis/tinytrader';

const initialState = {
  status: 'idle',
  data: {},
}

export const fetchMetricData = createAsyncThunk(
  'metric/fetchMetricData', async (ticker_id) => {
    const response = await tinytrader.get(`/metric/${ticker_id}/`);
    return response.data;
})

const metricSlice = createSlice({
  name: 'data',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchMetricData.fulfilled]: (state, action) => {
      state.data = action.payload;
      state.status = 'success';
    }
  }
})

export default metricSlice.reducer;