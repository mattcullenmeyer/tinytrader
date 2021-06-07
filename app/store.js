import { configureStore } from '@reduxjs/toolkit'
import tickerdataReducer from './reducers/tickerdataSlice';
import metadataReducer from './reducers/metadataSlice';


export default configureStore({
  reducer: {
    tickerdata: tickerdataReducer,
    metadata: metadataReducer,
  }
})