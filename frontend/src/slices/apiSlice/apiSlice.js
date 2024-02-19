import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const api = createApi({
	reducerPath: 'api',
	baseQuery: fetchBaseQuery({ baseUrl: 'http://coffee-gid.ddns.net/api/v1' }),
	tagTypes: ['Cards'],
	endpoints: build => ({
		getCards: build.query({
			query: args => {
				const { page, limit, offset, availables } = args;
				return {
					url: 'cafes',
					params: {
						limit,
						offset,
						page,
						availables,
					},
				};
			},
			providesTags: ['Cards'],
			// serializeQueryArgs: ({ endpointName }) => endpointName,
			// merge: (currentCache, newItems) => currentCache.push([...newItems]),
			// forceRefetch({ currentArg, previousArg }) {
			// 	return currentArg !== previousArg;
			// },
		}),
		getCardById: build.query({
			query: id => `cafes/${id}`,
		}),
	}),
});

export const { useGetCardsQuery, useGetCardByIdQuery, useLazyGetCardsQuery } = api;
