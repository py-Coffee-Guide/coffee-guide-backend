import React, { useState, useEffect } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import queryString from 'query-string';

import { setCards, clearCards, setFiltered } from '../../slices/cardsSlice/cardsSlice';
import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';
import { reset } from '../../slices/offsetSlice/offsetSlice';

import ProtectedRoute from '../ProtectedRoute/ProtectedRoute';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Login from '../Login/Login';
import Footer from '../Footer/Footer';
import CardMedium from '../CardMedium/CardMedium';
import Favourites from '../Favourites/Favourites';
import NotFound from '../NotFound/NotFound';
import Register from '../Register/Register';
import Profile from '../Profile/Profile';
import Preloader from '../Preloader/Preloader';

import styles from './App.module.scss';

function App() {
	const [loggedIn, setLoggedIn] = useState(!!localStorage.token);
	const [searchSuccess, setSearchSuccess] = useState(true);

	const tokenCheck = () => {
		if (localStorage.token) {
			setLoggedIn(true);
		}
	};

	useEffect(() => {
		tokenCheck();
	}, []);

	const dispatch = useDispatch();
	const filters = useSelector(state => state.cards.filters);
	const query = useSelector(state => state.cards.query);
	const offsetCounter = useSelector(state => state.offset);
	const filtered = useSelector(state => state.cards.filtered);

	const { data, isLoading, isSuccess, isFetching, refetch } = useGetCardsQuery(
		{
			name: query,
			address: query,
			page: offsetCounter,
			availables: queryString.stringify({ availables: [...filters] }),
		},
		{ refetchOnMountOrArgChange: false },
	);

	useEffect(() => {
		dispatch(reset());
		if (isSuccess && !query) {
			dispatch(setCards(data.results));
		}
		if (query && isSuccess) {
			dispatch(setFiltered(data.results));
		}
		if (query && data.results.length === 0) {
			setSearchSuccess(false);
		}
	}, [data]);

	if (isLoading) {
		return <Preloader />;
	}

	return (
		<div className={styles.root}>
			<Header />
			<Routes>
				<Route path="/" element={<Main isSearch={searchSuccess} data={data} />} />
				<Route path="/signin" element={<Login />} />
				<Route path="/card/:cardId" element={<CardMedium />} />
				<Route path="/signup" element={<Register />} />
				<Route path="/favourites" element={<Favourites />} />
				<Route path="/profile" element={<ProtectedRoute element={Profile} loggedIn={loggedIn} />} />
				<Route path="*" element={<NotFound />} />
			</Routes>
			<Footer />
		</div>
	);
}

export default App;
