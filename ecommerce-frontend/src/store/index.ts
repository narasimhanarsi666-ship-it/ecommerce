import { create } from 'zustand';

type CartState = { total: number, setTotal: (t:number)=>void }
export const useCartStore = create<CartState>((set)=>({ total: 0, setTotal: (t)=>set({ total: t }) }));
