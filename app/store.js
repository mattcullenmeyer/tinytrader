import { configureStore } from '@reduxjs/toolkit'
import tickerReducer from './tickerSlice';
import metadataReducer from './metadataSlice';


export default configureStore({
  reducer: {
    ticker: tickerReducer,
    metadata: metadataReducer,
  }
})