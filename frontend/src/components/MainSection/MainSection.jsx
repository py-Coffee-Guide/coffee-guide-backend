import styles from './MainSection.module.scss';

import Cards from '../Cards/Cards';
import MapComponent from '../Map/MapComponent';

function MainSection({ isSearch, data }) {
	return (
		<section className={styles.main}>
			{!isSearch ? (
				<div className={styles.message_container}>
					<h3 className={styles.heading}>Пo вашему запросу ничего не наӣдено </h3>
					<p className={styles.text}>Попробуӣте изменить параметры или ввести запрос по-другому </p>
				</div>
			) : (
				<>
					<p className={styles.text}>Подобрали для тебя кофейни</p>
					<div className={styles.container}>
						<Cards data={data} />
						<MapComponent />
					</div>
				</>
			)}
		</section>
	);
}

export default MainSection;
