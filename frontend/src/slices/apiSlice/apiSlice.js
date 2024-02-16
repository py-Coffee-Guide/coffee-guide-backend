import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const api = createApi({
	reducerPath: 'api',
	baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/v1/' }),
	tagTypes: ['Cards'],
	endpoints: build => ({
		getCards: build.query({
			query: args => {
				const { page, roasters, tags, alternatives, limit, offset } = args;
				return {
					url: 'cafes',
					params: {
						limit,
						offset,
						page,
						roasters,
						tags,
						alternatives,
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
