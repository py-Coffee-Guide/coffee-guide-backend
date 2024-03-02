import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import cn from 'classnames';
import { clearCards } from '../../slices/cardsSlice/cardsSlice';
import BackButton from '../../assets/ui-kit/BackButton/BackButton';
import CardSmall from '../CardSmall/CardSmall';
import styles from './Favourites.module.scss';

function Favourites() {
	const dispatch = useDispatch();
	const theme = useSelector(state => state.theme);
	const saved = useSelector(state => state.cards.favourites);
	const cardlistClassName = cn(styles.cardlist, styles.cardlist_favourite);

	// useEffect(() => {
	// 	dispatch(clearCards());
	// }, []);

	return (
		<section className={styles.container}>
			<div className={styles.back_button}>
				<BackButton type="button" theme={theme} text="Назад" />
			</div>
			{saved.length === 0 && (
				<div className={styles.no_favourites}>
					<p className={styles.text}>В избранном пока ничего нет.</p>
					<div className={theme === 'light' ? styles.coffee_cup : styles.coffee_cup_dark} />
				</div>
			)}

			<div className={cardlistClassName}>
				<ul>
					{saved.map(item => (
						<li key={item.id}>
							<CardSmall card={item} />
						</li>
					))}
				</ul>
			</div>
		</section>
	);
}

export default Favourites;
