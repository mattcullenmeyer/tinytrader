import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import tinytrader from './apis/tinytrader';
//import axios from 'axios';

const initialState = {
  data: {}
}

export const fetchTicker = createAsyncThunk('ticker/fetchTicker', async () => {
  const response = await tinytrader.get('/ticker/AAPL/');
  console.log(response.data);
  return response.data;
})

const tickerSlice = createSlice({
  name: 'data',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchTicker.fulfilled]: (state, action) => {
      //state.ticker = state.ticker.concat(action.payload)
      //return action.payload;
      state.data = action.payload;
    }
  }
})

export default tickerSlice.reducer;


/*
export const tickerSlice = createSlice({
  name: 'ticker',
  initialState: {
    value: ''
  },
  reducers: {
    update: (state, action) => {
      state.value = action.payload
    }
  }
})

export const { update } = tickerSlice.actions

export default tickerSlice.reducer
*/