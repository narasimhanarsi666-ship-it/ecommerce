import { useState } from 'react';
export default function CouponInput({ onApply }:{ onApply: (code:string)=>void }){
  const [code, setCode] = useState('');
  return (
    <div>
      <input value={code} onChange={e=>setCode(e.target.value)} placeholder="Enter coupon"/>
      <button onClick={()=>onApply(code)}>Apply</button>
    </div>
  );
}
