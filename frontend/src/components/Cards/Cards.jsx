import styles from './Cards.module.scss';

import CardSmall from '../CardSmall/CardSmall';
import { cards } from '../../utils/cards';

function Cards() {
	return (
		<div className={styles.container}>
			<ul>
				{cards.map(item => (
					<li key={item.id}>
						<CardSmall card={item} />
					</li>
				))}
			</ul>
		</div>
	);
}

export default Cards;
