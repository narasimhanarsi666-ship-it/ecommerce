import { render, screen } from '@testing-library/react';
import CartSummary from '../../src/components/cart/CartSummary';

test('renders totals', () => {
  render(<CartSummary cart={{items:[{sku:'SKU-1', qty:2, price:100}], subtotal:200, total:200}} />);
  expect(screen.getByText(/Subtotal: ₹200.00/)).toBeInTheDocument();
});
