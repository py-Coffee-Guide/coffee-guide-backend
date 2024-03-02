import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import queryString from 'query-string';

import { setCards, clearCards, setFiltered } from '../../slices/cardsSlice/cardsSlice';
import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';

import { increment } from '../../slices/offsetSlice/offsetSlice';

import CardSmall from '../CardSmall/CardSmall';
import styles from './Cards.module.scss';

function Cards({ data }) {
	const dispatch = useDispatch();
	const card = useSelector(state => state.cards.cards);

	const handleClick = () => {
		dispatch(increment());
	};

	return (
		<div className={styles.container}>
			<ul>
				{card?.map(card => (
					<li key={card.id}>
						<CardSmall card={card} />
					</li>
				))}
			</ul>
			{data.next !== null && (
				<button type="button" className={styles.more} onClick={handleClick}>
					Показать больше кофеен
				</button>
			)}
		</div>
	);
}

export default Cards;
