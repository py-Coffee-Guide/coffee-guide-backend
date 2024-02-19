import { createSlice } from '@reduxjs/toolkit';
import { useSelector } from 'react-redux';

const offsetSlice = createSlice({
	name: 'offset',
	initialState: 1,
	reducers: {
		increment: state => state + 1,
	},
});

export const { increment } = offsetSlice.actions;
export default offsetSlice.reducer;
