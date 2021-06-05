import { createSlice } from '@reduxjs/toolkit'

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