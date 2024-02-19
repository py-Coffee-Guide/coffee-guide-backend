import { useState } from 'react';
import { useForm } from 'react-hook-form';

import cn from 'classnames';
import styles from './NewCoffeeshop.module.scss';
import CheckBox from '../../assets/ui-kit/CheckBox/CheckBox';
import Button from '../../assets/ui-kit/Button/Button';
import CloseButton from '../../assets/ui-kit/CloseButton/CloseButton';

import { BASE_TAGS, SPECIAL_EXTRAS } from '../../utils/constants';

function NewCoffeeshop({ onClose }) {
	const [showPopupCoffeeTypes, setShowPopupCoffeeTypes] = useState(false);
	const [showPopupAlternatives, setShowPopupAlternatives] = useState(false);
	const [textHidden, setTextHidden] = useState(true);
	const inputTimeClassName = cn(styles.input_item, styles.input_medium);

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
			<form className={styles.container_main}>
				<ul className={styles.input_list}>
					<li className={styles.input_container}>
						<label htmlFor="cafe_name" className={styles.input_label}>
							Название кофейни
						</label>
						<input
							type="text"
							id="cafe_name"
							className={styles.input_item}
							placeholder="Название"
						/>
					</li>
					<li className={styles.input_container}>
						<label htmlFor="cafe_name" className={styles.input_label}>
							Адрес
						</label>
						<input
							type="text"
							id="cafe_name"
							className={styles.input_item}
							placeholder="Введите адрес"
						/>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Пн- Пт
							</label>
							<div>
								<input
									type="text"
									id="cafe_schedule"
									className={inputTimeClassName}
									placeholder="С"
								/>
								<input
									type="text"
									id="cafe_schedule"
									className={inputTimeClassName}
									placeholder="До"
								/>
							</div>
						</div>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Сб - Вс
							</label>
							<div className={styles.input_aligner}>
								<div style={{ marginBottom: '18px' }}>
									<input
										type="text"
										id="cafe_schedule"
										className={inputTimeClassName}
										placeholder="С"
									/>
									<input
										type="text"
										id="cafe_schedule"
										className={inputTimeClassName}
										placeholder="До"
									/>
								</div>
								<CheckBox text="Как в будни" />
								<CheckBox text="Круглосуточно" />
							</div>
						</div>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_drink" className={styles.input_label}>
								Напитки
							</label>
							<div className={styles.input_aligner} style={{ flexDirection: 'row' }}>
								<input
									type="text"
									id="cafe_drink"
									className={inputTimeClassName}
									placeholder="Напиток"
								/>
								<input
									type="text"
									id="cafe_drink"
									className={inputTimeClassName}
									style={{ width: '76px' }}
									placeholder="&#8381;"
								/>
							</div>
						</div>
						<p>+ добавить</p>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_tags" className={styles.input_label}>
								Доступные опции
							</label>
							<div className={styles.input_aligner}>
								<div>
									{BASE_TAGS.map(item => (
										<CheckBox key={item.id} text={item.text} />
									))}
								</div>
							</div>
						</div>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_roasters" className={styles.input_label}>
							Обжарщики
						</label>
						<input type="text" id="cafe_roasters" className={styles.input_item} />
					</li>

					<li className={styles.input_container}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Доступные опции
							</label>
							<div className={styles.input_aligner}>
								<div>
									{SPECIAL_EXTRAS.map(item => (
										<CheckBox key={item.id} text={item.text} />
									))}
								</div>
							</div>
						</div>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_description" className={styles.input_label}>
							Описание
						</label>
						<textarea
							type="text"
							id="cafe_description"
							className={styles.input_item}
							style={{ height: '128px' }}
						/>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_image" className={styles.input_label}>
							Фото на обложку
						</label>
						<textarea
							type="text"
							id="cafe_image"
							className={styles.input_item}
							style={{ height: '128px' }}
						/>
					</li>
				</ul>
				<Button text="Добавить кофейню" type="submit" size="medium" />
			</form>
		</section>
	);
}

export default NewCoffeeshop;
