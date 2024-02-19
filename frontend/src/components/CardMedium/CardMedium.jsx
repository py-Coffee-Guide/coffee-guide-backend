import { useSelector } from 'react-redux';
import { useLocation } from 'react-router-dom';

import cn from 'classnames';
import styles from './CardMedium.module.scss';

import BackButton from '../../assets/ui-kit/BackButton/BackButton';
import FavouritesButton from '../../assets/ui-kit/FavouritesButton/FavouritesButton';
import nullImage from '../../assets/images/logo.svg';

import { useGetCardByIdQuery } from '../../slices/apiSlice/apiSlice';

function CardMedium() {
	const location = useLocation();
	const theme = useSelector(state => state.theme);
	const { data = {}, isLoading } = useGetCardByIdQuery(location.state.key);

	if (isLoading) {
		return <p>LOADING....</p>;
	}

	const {
		address,
		alternatives,
		description,
		id,
		image,
		name,
		roasters,
		schedules,
		additionals,
		drinks,
	} = data;
	const imgClassName = cn(styles.img, { [styles.img_null]: !image });

	console.log(data);

	return (
		<section className={styles.container}>
			<BackButton type="button" theme={theme} text="Назад" />

			<div className={styles.heading}>
				<div className={styles.title}>
					<h1>{name}</h1>
					<p>{description}</p>
				</div>
				<div className={styles.map}>
					<div className={styles.map_mini} />
					<button className={styles.button} type="button">
						Построить маршрут
					</button>
				</div>
				<div className={styles.info}>
					<div className={styles.info_container}>
						<div className={styles.point_icon} />
						<p>{address.name}</p>
					</div>
					<div className={styles.info_container}>
						<div className={styles.schedule_icon} />
						<ul className={styles.schedules}>
							{schedules.map(item => (
								<li key={item.id} className={styles.schedules_item}>
									<p> {item.name}</p>
									<p> {item.start.slice(0, -3)}</p>
									<p> {item.end.slice(0, -3)}</p>
								</li>
							))}
						</ul>
					</div>
				</div>
			</div>
			<div className={styles.desription}>
				<div className={styles.photo}>
					<img className={imgClassName} src={!image ? nullImage : image} alt="фото кофейни" />
					<div className={styles.favourites}>
						{' '}
						<FavouritesButton type="button" card={data} />
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
							{drinks.map(item => (
								<li key={item.id}>{`${item.name} ${item.cost} ₽`} </li>
							))}
						</ul>
					</div>

					<h3 className={cn(styles.tag3, styles.tag)}>Обжарщик</h3>
					<ul className={cn(styles.list3, styles.list)}>
						{roasters.map(item => (
							<li key={item.id}>
								<p>{item.name}</p>
							</li>
						))}
					</ul>
					<h3 className={cn(styles.tag4, styles.tag)}>Альтернатива</h3>
					<div className={cn(styles.list4, styles.list)}>
						{alternatives.map(item => (
							<li key={item.id}>
								<p>{item.name}</p>
							</li>
						))}
					</div>
					<h3 className={cn(styles.tag5, styles.tag)}>Дополнительно</h3>
					<ul className={cn(styles.list5, styles.list)}>
						{additionals.map(item => (
							<li key={item.id}>
								<p>{item.name}</p>
							</li>
						))}
					</ul>
				</div>
			</div>
		</section>
	);
}

export default CardMedium;
