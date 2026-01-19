import { api } from './api';
export async function getCart(userId: string) {
  const { data } = await api.get(`/api/cart?user_id=${userId}`);
  return data;
}
export async function addItem(userId: string, sku: string, qty: number) {
  const { data } = await api.post(`/api/cart/item`, { user_id: userId, sku, qty });
  return data;
}
