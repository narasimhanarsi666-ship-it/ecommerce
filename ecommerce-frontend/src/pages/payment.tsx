import { useState } from 'react';
import { pay } from '../services/paymentApi';

export default function Payment(){
  const [result,setResult] = useState<any>(null);
  return (
    <div>
      <h1>Payment</h1>
      <button onClick={async()=> setResult(await pay('u1','creditcard',100))}>Pay ₹100</button>
      {result && <pre>{JSON.stringify(result,null,2)}</pre>}
    </div>
  );
}
