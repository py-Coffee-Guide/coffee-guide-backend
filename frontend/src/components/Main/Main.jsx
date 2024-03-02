import styles from './Main.module.scss';

import TagSection from '../TagSection/TagSection';
import MainSection from '../MainSection/MainSection';

function Main({ isSearch, data }) {
	return (
		<main className={styles.main}>
			<TagSection />
			<MainSection isSearch={isSearch} data={data} />
		</main>
	);
}

export default Main;
