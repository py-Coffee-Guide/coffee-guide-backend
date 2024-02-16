import { createSlice } from '@reduxjs/toolkit';

const initialState = [];

const filteredCardsSlice = createSlice({
	name: 'filteredCards',
	initialState,
	reducers: {
		resetFilteredCards: () => initialState,
		setFilteredCards: (state, action) => [...state, ...action.payload],
	},
});

export const { setFilteredCards, resetFilteredCards } = filteredCardsSlice.actions;
export default filteredCardsSlice.reducer;
