import React from 'react';
import styles from './Preloader.module.scss';

function Preloader() {
	return (
		<section className={styles.preloader}>
			<div className={styles.preloader__container}>
				<span className={styles.preloader__round} />
			</div>
		</section>
	);
}

export default Preloader;
