import { configureStore } from '@reduxjs/toolkit'
import tickerReducer from './tickerSlice';


export default configureStore({
  reducer: {
    ticker: tickerReducer,
  }
})