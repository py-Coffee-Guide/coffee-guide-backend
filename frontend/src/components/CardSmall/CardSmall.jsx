import styles from './CardSmall.module.scss';
import Button from '../../assets/ui-kit/TagButton/TagButton';

function CardSmall({ card, onSave, onDelete }) {
	const { adress, name, schedule, image } = card;
	return (
		<div className={styles.card}>
			<div className={styles.photo_container}>
				<img className={styles.photo} src={image} alt="фото кофейни" />
				<div className={styles.favourite}>
					<Button preset="action" additions="active" aria-label="добавить в избранное" />
				</div>
				{/* <div className={styles.close}>
					<Button preset="action" additions="close" aria-label="удалить из избранного" />
				</div> */}
			</div>

			<div className={styles.info}>
				<h3 className={styles.title}>{name}</h3>
				<p className={styles.text}>{adress}</p>
				<p className={styles.text}>{schedule[0].text}</p>
				<p className={styles.text}>{schedule[1].text}</p>
			</div>
		</div>
	);
}

export default CardSmall;
