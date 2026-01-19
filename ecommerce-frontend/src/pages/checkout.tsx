import CheckoutForm from '../components/checkout/CheckoutForm';
import PriceBreakdown from '../components/checkout/PriceBreakdown';

export default function Checkout(){
  return (
    <div>
      <h1>Checkout</h1>
      <CheckoutForm />
      <PriceBreakdown subtotal={100} shipping={0} tax={0} total={100} />
    </div>
  );
}
