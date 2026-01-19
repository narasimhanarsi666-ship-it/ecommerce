import { formatINR } from '../../utils/price';
export default function PriceBreakdown({subtotal,shipping,tax,total}:{subtotal:number,shipping:number,tax:number,total:number}){
  return (
    <div>
      <h3>Price</h3>
      <p>Subtotal: {formatINR(subtotal)}</p>
      <p>Shipping: {formatINR(shipping)}</p>
      <p>Tax: {formatINR(tax)}</p>
      <p><b>Total: {formatINR(total)}</b></p>
    </div>
  );
}
