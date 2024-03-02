import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {
	clearCards,
	clearFiltered,
	clearQuery,
	clearFilters,
} from '../../slices/cardsSlice/cardsSlice';
import { reset } from '../../slices/offsetSlice/offsetSlice';

import logo from '../../assets/images/logo.svg';
import logoDark from '../../assets/images/logo-dark.svg';
import icon from '../../assets/images/profile-icon.svg';
import iconDark from '../../assets/images/profile-icon-dark.svg';
import Theme from '../Theme/Theme';
import SearchSection from '../SearchSection/SearchSection';

import styles from './Header.module.scss';

const FullRenderedSection = () => {
	const theme = useSelector(state => state.theme);

	return (
		<>
			<SearchSection />
			<nav className={styles.align_container}>
				<Link to="/favourites" className={styles.favourites}>
					<div className={theme === 'light' ? styles.icon : styles.icon_dark} />
					<p className={styles.text}>Избранное</p>
				</Link>
				<Theme />
			</nav>
		</>
	);
};

function Header() {
	const location = useLocation();
	const dispatch = useDispatch();
	const navigate = useNavigate();
	const theme = useSelector(state => state.theme);
	const offset = useSelector(state => state.offset);

	const handleClick = () => {
		if (location.pathname !== '/') {
			navigate('/', { replace: true });
		}
		dispatch(clearFiltered());
		dispatch(clearQuery());
		dispatch(clearCards());
		dispatch(reset());
		navigate(0);
	};

	return (
		<header className={styles.header}>
			<div className={styles.container}>
				<div>
					<button type="button" onClick={handleClick} className={styles.logo}>
						{theme === 'light' ? (
							<img className={styles.logo} src={logo} alt="Лого" />
						) : (
							<img className={styles.logo} src={logoDark} alt="Лого" />
						)}
					</button>
				</div>

				{!['/signin', '/signup', '/profile'].some(path => location.pathname.match(path)) ? (
					<FullRenderedSection />
				) : (
					<nav className={styles.align_container}>
						{location.pathname.match('/profile') && (
							<>
								<div className={styles.profile}>
									<img
										src={theme === 'light' ? icon : iconDark}
										className={styles.profile_icon}
										alt="profile"
									/>
									<p className={styles.text}>pochta@email.ru</p>
								</div>
								<div className={styles.button_container}>
									<button type="button" className={styles.button_quit} onClick={handleClick}>
										Выйти
									</button>
								</div>
							</>
						)}
						<Theme />
					</nav>
				)}
			</div>
		</header>
	);
}

export default Header;
