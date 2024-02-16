import { useNavigate } from 'react-router-dom';
import cn from 'classnames';
import styles from './CardMedium.module.scss';
// import Button from '../../assets/ui-kit/Button/Button';

import photo from '../../assets/images/photo/66be5a14bddf717c1205b56a1ed80d15.jpg';

function CardSmall({ card, onSave, onDelete }) {
	const navigate = useNavigate();

	return (
		<section className={styles.container}>
			<button className={styles.back} onClick={() => navigate(-1)}>
				<div className={styles.back_icon} />
				Назад
			</button>
			<div className={styles.heading}>
				<div className={styles.title}>
					<h1>Adept x Common Coffee</h1>
					<p>
						У нас всегда есть свежеобжаренный кофе, который оценят любители этого напитка. В
						ассортименте вы найдёте разные сорта и смеси со всех концов света.
					</p>
				</div>
				<div className={styles.map}>
					<div className={styles.map_mini} />
					<button className={styles.button} type="button">
						Построить маршрут
					</button>
				</div>
				<div className={styles.info}>
					<div className={styles.point_icon} />
					<p>Бережсковская набережная, 20с13</p>
					<div className={styles.schedule_icon} />
					<div>
						{' '}
						<p>Пн—Пт 9:00—19:00</p>
						<p>Сб—Вс Выходной</p>
					</div>
				</div>
			</div>
			<div className={styles.desription}>
				<div className={styles.photo}>
					<img className={styles.img} src={photo} alt="" />
					<div className={styles.favourites}>
						{' '}
						<button type="button" className={styles.save} aria-label="добавить в избранное" />
					</div>
				</div>
				<div className={styles.features}>
					<h3 className={cn(styles.tag1, styles.tag)}>Доступно</h3>
					<ul className={cn(styles.list1, styles.list)}>
						<li>Безлактозное</li>
						<li>Submarine</li>
						<li>Альтернатива</li>
					</ul>

					<h3 className={cn(styles.tag2, styles.tag)}>Напитки</h3>
					<div className={cn(styles.list2)}>
						<ul className={cn(styles.list)}>
							<li>Эспрессо: 200 ₽ </li>
							<li>Капучино: 300 ₽ </li>
							<li>Американо: 300 ₽ </li>
						</ul>
						<ul className={cn(styles.list)}>
							<li>Латте: 200 ₽ </li>
							<li>Флэт-уайт: 400 ₽ </li>
							<li>Фильтр-кофе: 400 ₽ </li>
						</ul>
					</div>

					<h3 className={cn(styles.tag3, styles.tag)}>Обжарщик</h3>
					<ul className={cn(styles.list3, styles.list)}>
						<li>Adept x Common Coffee</li>
					</ul>
					<h3 className={cn(styles.tag4, styles.tag)}>Альтернатива</h3>
					<div className={cn(styles.list4, styles.list)}>
						<ul className={cn(styles.list)}>
							<li>V60</li>
							<li>Кемекс</li>
						</ul>
						<ul className={cn(styles.list)}>
							<li>Френч-пресс</li>
							<li>Аэропресс</li>
						</ul>
					</div>
					<h3 className={cn(styles.tag5, styles.tag)}>Дополнительно</h3>
					<ul className={cn(styles.list5, styles.list)}>
						<li>Можно с животными</li>
						<li>Продажа зерна </li>
						<li>Декаф </li>
					</ul>
				</div>
			</div>
		</section>
	);
}

export default CardSmall;
