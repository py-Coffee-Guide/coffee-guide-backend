// import { useSelector } from 'react-redux';
import { useState, useEffect } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import { useSelector } from 'react-redux';

import { api } from '../../utils/Api';

import Header from '../Header/Header';
import Main from '../Main/Main';
import Login from '../Login/Login';
import Footer from '../Footer/Footer';
import CardMedium from '../CardMedium/CardMedium';
import Favourites from '../Favourites/Favourites';
import NotFound from '../NotFound/NotFound';
import Register from '../Register/Register';
import Profile from '../Profile/Profile';

import { card } from '../../utils/card';

import styles from './App.module.scss';

function App() {
	const location = useLocation();
	const theme = useSelector(state => state.theme);

	// const [cards, setCards] = useState([]);

	// useEffect(() => {
	// 	Promise.all([api.getOrganizations()])
	// 		.then(([card]) => {
	// 			setCards(card.results);
	// 		})
	// 		.catch(err => {
	// 			console.log(err);
	// 		});
	// }, []);

	// a0303f06-4ef8-4bd2-bef5-7e2e5e6b3ff6
	// const { user } = useSelector(state => state);
	// card={cards.find(item => item.id === location.pathname.replace('/card/', ''))}
	return (
		<div className={styles.root}>
			<Header />
			<Routes>
				<Route path="/" element={<Main />} />
				<Route path="/card/:cardId" element={<CardMedium />} />
				<Route path="/signin" element={<Login />} />
				<Route path="/signup" element={<Register />} />
				<Route path="/favourites" element={<Favourites />} />
				<Route path="/profile" element={<Profile />} />
				<Route path="*" element={<NotFound />} />
			</Routes>
			<Footer />
		</div>
	);
}

export default App;
