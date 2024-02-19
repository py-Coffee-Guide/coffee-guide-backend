import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import BackButton from '../../assets/ui-kit/BackButton/BackButton';
import CardSmall from '../CardSmall/CardSmall';
import styles from './Favourites.module.scss';

function Favourites() {
	const theme = useSelector(state => state.theme);
	const saved = useSelector(state => state.cards.favourites);

	return (
		<section className={styles.container}>
			<div className={styles.back_button}>
				<BackButton type="button" theme={theme} text="Назад" />
			</div>
			<div className={styles.cardlist}>
				<ul>
					{saved.map(item => (
						<li key={item.id}>
							<CardSmall card={item} />
						</li>
					))}
				</ul>
			</div>
			{/* <Cards /> */}
		</section>
	);
}

export default Favourites;
