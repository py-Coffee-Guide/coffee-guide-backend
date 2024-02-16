import styles from './SearchSection.module.scss';
import Button from '../../assets/ui-kit/Button/Button';

function SearchSection() {
	return (
		<section className={styles.container}>
			<div className={styles.input_container}>
				<input className={styles.input} placeholder="Название кофеӣни / адрес" />
			</div>
			<Button text="найти" size="small" />
		</section>
	);
}

export default SearchSection;
