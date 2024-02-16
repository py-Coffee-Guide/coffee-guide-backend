import { createSlice } from '@reduxjs/toolkit';

const initialState = {
	name: '',
	email: '',
	isLoggedIn: false,
};

const userSlice = createSlice({
	name: 'user',
	initialState,
	reducers: {},
});

const { actions, reducer } = userSlice;

export default reducer;
// export const { } = actions;
