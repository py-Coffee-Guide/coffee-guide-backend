import { useState, useEffect } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import cn from 'classnames';
import styles from './Login.module.scss';
import { useLoginMutation } from '../../slices/apiSlice/apiSlice';
import { setUser } from '../../slices/userSlice/userSlice';

import Button from '../../assets/ui-kit/Button/Button';

function Login() {
	const navigate = useNavigate();

	useEffect(() => {
		if (localStorage.token) {
			navigate('/profile', { replace: true });
		}
	}, [navigate]);

	const {
		register,
		watch,
		handleSubmit,
		reset,
		formState: { errors },
	} = useForm({ defaultValues: { username: '', password: '' }, mode: 'onChange' });

	const [login, { isError }] = useLoginMutation();
	const watchInputs = watch();

	const handleLogin = async () => {
		if (watchInputs) {
			await login(watchInputs)
				.unwrap()
				.then(data => {
					if (data.auth_token) {
						localStorage.setItem('token', data.auth_token);
						navigate('/profile', { replace: true });
					}
				})
				.catch(rejected => console.error(rejected));
		}
	};

	const onSubmit = data => {
		reset();
	};

	const inputItemClassName = type => cn(styles.input, [errors[type] && styles.input_error]);

	return (
		<section className={styles.container}>
			<div className={styles.aligner}>
				<form className={styles.form} onSubmit={handleSubmit(onSubmit)}>
					<div className={styles.input_container}>
						<input
							{...register('username', {
								required: 'Необходимо ввести почту или ИНН',
								pattern: {
									value: /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)/g,
									message: 'Введите корректный email',
								},
							})}
							className={inputItemClassName('email')}
							placeholder="Почта / ИНН"
						/>
						{errors.email && <span className={styles.error}>{errors.email?.message}</span>}
					</div>
					<div className={styles.input_container}>
						<input
							type="password"
							{...register('password', {
								required: 'Необходимо ввести пароль',
							})}
							className={inputItemClassName('password')}
							placeholder="Пароль"
						/>
						{errors.password && <span className={styles.error}>{errors.password?.message}</span>}
					</div>
					<Button onClick={() => handleLogin()} type="submit" size="large" text="Войти" />
				</form>
				<div className={styles.links}>
					<p>Впервые у нас?</p>
					<NavLink to="/signup" className={styles.link}>
						Зарегистрироваться
					</NavLink>
				</div>
			</div>
			<p className={styles.text}>
				В случае если вы забыли пароль или у вас возникли вопросы, напишите нам admin@gmail.com
			</p>
		</section>
	);
}

export default Login;
