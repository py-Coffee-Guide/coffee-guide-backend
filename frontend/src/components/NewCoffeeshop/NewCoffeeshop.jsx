import { useState } from 'react';

import styles from './NewCoffeeshop.module.scss';
import CheckBox from '../../assets/ui-kit/CheckBox/CheckBox';
import Button from '../../assets/ui-kit/Button/Button';
import CloseButton from '../../assets/ui-kit/CloseButton/CloseButton';

function NewCoffeeshop({ onClose }) {
	const [showPopupCoffeeTypes, setShowPopupCoffeeTypes] = useState(false);
	const [showPopupAlternatives, setShowPopupAlternatives] = useState(false);
	const [textHidden, setTextHidden] = useState(true);

	const handleInputClick = () => {
		setTextHidden(false);
	};

	const handleInputCoffee = () => {
		setShowPopupCoffeeTypes(!showPopupCoffeeTypes);
	};

	const handleCheckboxChange = () => {
		setShowPopupAlternatives(!showPopupAlternatives);
	};

	return (
		<section className={styles.container}>
			<div className={styles.close}>
				<CloseButton onClick={onClose} size="default" />
			</div>
			<div className={styles.container_main}>
				<div className={styles.container}>
					<h3 className={styles.title}> Название кофейни</h3>
					<input className={styles.input_name} placeholder="Название" />
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> Адрес</h3>
					<input className={styles.input_direction} />
				</div>
				<h3 className={styles.schedule}> График работы</h3>
				<div className={styles.container}>
					<h3 className={styles.title}> ПН - ПТ</h3>
					<input className={styles.input_time} placeholder="00:00" />
					<input className={styles.input_time} placeholder="00:00" />
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> СБ - ВС</h3>
					<input className={styles.input_time} placeholder="00:00" />
					<input className={styles.input_time} placeholder="00:00" />
				</div>
				<div className={styles.container_days}>
					<div className={styles.container_option}>
						<CheckBox />
						<h3 className={styles.title_option}> Как в будни </h3>
					</div>
					<div className={styles.container_option}>
						<CheckBox />
						<h3 className={styles.title_option}> Круглосуточно </h3>
					</div>
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> Напитки</h3>
					<div>
						<input className={styles.input_type} onClick={handleInputCoffee} />
						{showPopupCoffeeTypes && (
							<div className={styles.coffee_types_container}>
								<h3 className={styles.popup_coffee}> Эспрессо </h3>
								<h3 className={styles.popup_coffee}> Капучино </h3>
								<h3 className={styles.popup_coffee}> Американо </h3>
								<h3 className={styles.popup_coffee}> Фильтр - кофе </h3>
								<h3 className={styles.popup_coffee}> Латте </h3>
								<h3 className={styles.popup_coffee}> Флет Уайт </h3>
							</div>
						)}
						<input className={styles.input_price} />
					</div>
					<h3 className={styles.title_price}> руб </h3>
				</div>
				<button className={styles.add_button} type="button">
					{' '}
					+ добавить напиток
				</button>
				<div className={styles.container}>
					<h3 className={styles.title}> Доступные опции </h3>
					<div className={styles.container_options}>
						<div className={styles.container_option}>
							<CheckBox onClick={handleCheckboxChange} />
							<h3 className={styles.title_option}> Альтернатива </h3>
						</div>
						{showPopupAlternatives && (
							<div className={styles.alternative_options}>
								<div className={styles.container_option}>
									<CheckBox />
									<h3 className={styles.title_option}> V60 </h3>{' '}
								</div>
								<div className={styles.container_option}>
									<CheckBox />
									<h3 className={styles.title_option}> Кемекс </h3>
								</div>
								<div className={styles.container_option}>
									<CheckBox />
									<h3 className={styles.title_option}> Аэропресс </h3>
								</div>
								<div className={styles.container_option}>
									<CheckBox />
									<h3 className={styles.title_option}> Френч-пресс </h3>{' '}
								</div>
							</div>
						)}
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Безлактозное молоко </h3>
						</div>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Сварщица </h3>
						</div>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> La Marzocco </h3>
						</div>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Submarine </h3>
						</div>
					</div>
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> Обжарщики </h3>
					<input className={styles.input_roaster} />
				</div>
				<button className={styles.add_button} type="button">
					{' '}
					+ добавить обжарщика
				</button>
				<div className={styles.container}>
					<h3 className={styles.title}> Дополнительные опции </h3>
					<div className={styles.container_options}>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Можно с животными </h3>
						</div>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Продажа зерна </h3>
						</div>
						<div className={styles.container_option}>
							<CheckBox />
							<h3 className={styles.title_option}> Декаф </h3>
						</div>
					</div>
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> Описание </h3>
					<input className={styles.description} />
				</div>
				<div className={styles.container}>
					<h3 className={styles.title}> Фото на обложку </h3>
					<input className={styles.photo} onClick={handleInputClick} />
					{textHidden && (
						<h3 className={styles.photo_text}>
							<span className={styles.photo_span}>Выберите файл</span> или перетащите его сюда{' '}
						</h3>
					)}
				</div>
				<div className={styles.container_days}>
					<Button text="Добавить кофейню" type="submit" size="medium" />
				</div>
			</div>
		</section>
	);
}

export default NewCoffeeshop;
