import { formatINR } from '../../utils/price';
export default function CartSummary({ cart }:{ cart:any }){
  return (
    <div>
      <h2>Summary</h2>
      <ul>
        {cart.items.map((i:any)=> (
          <li key={i.sku}>{i.sku} x {i.qty} @ {formatINR(i.price)}</li>
        ))}
      </ul>
      <p>Subtotal: {formatINR(cart.subtotal)}</p>
      <p>Total: {formatINR(cart.total)}</p>
    </div>
  );
}
