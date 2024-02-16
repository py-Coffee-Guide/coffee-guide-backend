import { configureStore } from '@reduxjs/toolkit';
import user from '../slices/userSlice/userSlice';
import themeReducer from '../slices/themeSlice/themeSlice';

const store = configureStore({
	reducer: {
		user,
		theme: themeReducer,
	},
});

export default store;
