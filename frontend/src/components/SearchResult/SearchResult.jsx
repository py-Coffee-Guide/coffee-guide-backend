import { useSelector, useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import cn from 'classnames';

import styles from './SearchResult.module.scss';
import CardMedium from '../CardMedium/CardMedium';

function SearchResult({ isVisible }) {
	const filteredCards = useSelector(state => state.filteredCards);

	const resultClassName = cn(
		styles.result_container,
		isVisible ? styles.popup_opened : styles.popup,
	);

	return (
		<div className={resultClassName}>
			<ul className={styles.result}>
				{filteredCards.slice(0, 4).map(item => (
					<li className={styles.item} key={item.id}>
						<Link to={`/card/${item.id}`} className={styles.link}>
							<p className={styles.title}>{item.name}</p>
							<address className={styles.address}>{item.address}</address>
						</Link>
					</li>
				))}
			</ul>
		</div>
	);
}

export default SearchResult;
