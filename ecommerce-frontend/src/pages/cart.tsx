import { useEffect, useState } from 'react';
import { getCart, addItem } from '../services/checkoutApi';
import CartSummary from '../components/cart/CartSummary';

export default function CartPage() {
  const [cart, setCart] = useState<any>(null);
  const userId = "u1";

  useEffect(() => { getCart(userId).then(setCart); }, []);

  return (
    <div>
      <h1>Cart</h1>
      <button onClick={async () => setCart(await addItem(userId, 'SKU-1', 1))}>Add SKU-1</button>
      {cart && <CartSummary cart={cart} />}
    </div>
  );
}
