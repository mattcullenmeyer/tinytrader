import { configureStore } from '@reduxjs/toolkit'
import tickerdataReducer from './reducers/tickerdataSlice';
import metadataReducer from './reducers/metadataSlice';
import metricReducer from './reducers/metricSlice';


export default configureStore({
  reducer: {
    tickerdata: tickerdataReducer,
    metadata: metadataReducer,
    metric: metricReducer,
  }
})