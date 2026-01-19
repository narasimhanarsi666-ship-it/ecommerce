import { api } from './api';
export async function pay(userId: string, method: string, amount: number){
  const { data } = await api.post('/api/payment/pay', { user_id: userId, method, amount });
  return data;
}
