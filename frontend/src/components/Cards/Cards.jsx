import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import { setCards } from '../../slices/cardsSlice/cardsSlice';
import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';

import { increment } from '../../slices/offsetSlice/offsetSlice';

import CardSmall from '../CardSmall/CardSmall';
import styles from './Cards.module.scss';

function Cards() {
	const dispatch = useDispatch();
	const card = useSelector(state => state.cards.cards);
	const offsetCounter = useSelector(state => state.offset);
	const { cards, isFetching, isLoading, isSuccess, isError } = useGetCardsQuery(
		{ page: offsetCounter },
		{
			selectFromResult: ({ data }) => ({
				cards: data?.results,
			}),
		},
	);

	const handleClick = () => {
		dispatch(increment());
		dispatch(setCards(cards));
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
			{!isError && (
				<button type="button" className={styles.more} onClick={handleClick}>
					Показать больше кофеен
				</button>
			)}
		</div>
	);
}

export default Cards;
