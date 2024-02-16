import { createSlice } from '@reduxjs/toolkit';

const favouritesSlice = createSlice({
	name: 'favourites',
	initialState: {
		favourites: JSON.parse(localStorage.getItem('favourite')) || [],
	},

	reducers: {
		addToFavourite: (state, action) => {
			if (!state.favourites.some(i => i.id === action.payload.id)) {
				state.favourites.push(action.payload);
				localStorage.setItem('favourite', JSON.stringify(state.favourites));
			} else {
				state.favourites = state.favourites.filter(i => i.id !== action.payload.id);
				localStorage.setItem('favourite', JSON.stringify(state.favourites));
			}
		},
	},
});

export const { addToFavourite } = favouritesSlice.actions;
export default favouritesSlice.reducer;
