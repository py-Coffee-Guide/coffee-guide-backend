import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/query';
import user from '../slices/userSlice/userSlice';
import { api } from '../slices/apiSlice/apiSlice';
import offsetSlice from '../slices/offsetSlice/offsetSlice';
import themeReducer from '../slices/themeSlice/themeSlice';
import cardsReducer from '../slices/cardsSlice/cardsSlice';

const store = configureStore({
	reducer: {
		[api.reducerPath]: api.reducer,
		user,
		offset: offsetSlice,
		theme: themeReducer,
		cards: cardsReducer,
	},
	middleware: getDefaultMiddleware => getDefaultMiddleware().concat(api.middleware),
});

// setupListeners(store.dispatch);
export default store;
