import styles from './Main.module.scss';

import SearchSection from '../SearchSection/SearchSection';
import TagSection from '../TagSection/TagSection';

import MainSection from '../MainSection/MainSection';
import HorizontalLine from '../HorizontalLine/HorizontalLine';

function Main() {
	return (
		<>
			<main className={styles.main}>
				<TagSection />
				<MainSection />
			</main>
			<HorizontalLine />
		</>
	);
}

export default Main;
