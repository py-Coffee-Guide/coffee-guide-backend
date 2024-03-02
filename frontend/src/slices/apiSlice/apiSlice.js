import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import queryString from 'query-string';

export const api = createApi({
	reducerPath: 'api',
	baseQuery: fetchBaseQuery({
		baseUrl: 'https://www.coffee-guide.ru/api/v1/',
		// baseUrl: 'http://localhost:8000/api/v1/',
		prepareHeaders: headers => {
			headers.set('Content-type', 'application/json');
			return headers;
		},
	}),
	tagTypes: ['Cards', 'Users'],
	endpoints: build => ({
		getCards: build.query({
			query: args => {
				const { page, availables, name, address } = args;
				return {
					url: `cafes?${availables}`,
					params: {
						...(page && !name && !address && { page }),
						...(name && { name }),
						...(address && { address }),
					},
				};
			},
			providesTags: ['Cards'],
		}),

		getCardById: build.query({
			query: id => `cafes/${id}`,
		}),

		addCard: build.mutation({
			query: body => ({
				url: 'cafes',
				method: 'POST',
				body,
			}),
			providesTags: result =>
				result
					? [...result.map(({ id }) => ({ type: 'Cards', id })), { type: 'Cards', id: 'LIST' }]
					: [{ type: 'Cards', id: 'LIST' }],
		}),

		// USER REDUCERS
		getUsers: build.query({
			query: () => 'users',
			providesTags: result =>
				result
					? [...result.map(({ id }) => ({ type: 'Users', id })), { type: 'Users', id: 'LIST' }]
					: [{ type: 'Users', id: 'LIST' }],
		}),

		addUser: build.mutation({
			query: body => ({
				url: 'users/',
				method: 'POST',
				body,
			}),
			invalidatesTags: [{ type: 'Users', id: 'LIST' }],
		}),

		login: build.mutation({
			query: body => ({
				url: 'auth/token/login/',
				method: 'POST',
				body,
			}),
		}),

		// deleteUser: build.mutation({
		// 	query: id => ({
		// 		url: `users/${id}/`,
		// 		method: 'DELETE',
		// 	}),
		// 	invalidatesTags: [{ type: 'Users', id: 'LIST' }],
		// }),
	}),
});

export const {
	useGetCardsQuery,
	useGetCardByIdQuery,
	useGetUsersQuery,
	useAddUserMutation,
	useLoginMutation,
	useDeleteUserMutation,
} = api;
