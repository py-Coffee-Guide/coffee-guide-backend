import logoPath from '../../assets/images/logo.svg';
import Button from '../../assets/ui-kit/TagButton/TagButton';
import Theme from '../Theme/Theme';
import SearchSection from '../SearchSection/SearchSection';

import styles from './Header.module.scss';

function Header() {
	return (
		<header className={styles.header}>
			<div className={styles.container}>
				<img className={styles.logo} src={logoPath} alt="Лого" />
				<SearchSection />
				<nav className={styles.align_container}>
					<div className={styles.favourites}>
						<div className={styles.icon} />
						<p>Избранное</p>
					</div>
					<Theme />
				</nav>
			</div>
		</header>
	);
}

export default Header;
