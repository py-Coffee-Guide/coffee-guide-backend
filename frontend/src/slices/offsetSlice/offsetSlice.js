import { createSlice } from '@reduxjs/toolkit';
import { useSelector } from 'react-redux';

const initialState = 1;

const offsetSlice = createSlice({
	name: 'offset',
	initialState,
	reducers: {
		increment: state => state + 1,
		reset: () => initialState,
	},
});

export const { increment, reset } = offsetSlice.actions;
export default offsetSlice.reducer;
