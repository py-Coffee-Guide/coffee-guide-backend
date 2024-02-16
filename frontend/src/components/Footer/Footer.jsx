import { NavLink } from 'react-router-dom';
import styles from './Footer.module.scss';

function Footer() {
	return (
		<footer className={styles.footer}>
			<div className={styles.container}>
				<p>Сделано студентами Яндекс Практикума</p>
				<div className={styles.aligner}>
					<NavLink to="/signup" className={styles.link}>
						<p>CoffeeGuide Pro</p>
					</NavLink>
					<p>&copy;Copyright 2024 CoffeeGuide</p>
				</div>
			</div>
		</footer>
	);
}

export default Footer;
