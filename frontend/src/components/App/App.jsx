// import { useSelector } from 'react-redux';
import { Routes, Route, useNavigate } from 'react-router-dom';

import Header from '../Header/Header';
import Main from '../Main/Main';
import Footer from '../Footer/Footer';
import CardMedium from '../CardMedium/CardMedium';

import styles from './App.module.scss';

function App() {
	// const { user } = useSelector(state => state);
	return (
		<div className={styles.root}>
			<Header />
			<Routes>
				<Route path="/" element={<Main />} />
				<Route path="/card" element={<CardMedium />} />
			</Routes>
			<Footer />
		</div>
	);
}

export default App;
