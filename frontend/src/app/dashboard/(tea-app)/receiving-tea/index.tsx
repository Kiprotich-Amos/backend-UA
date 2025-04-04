import React, { useState } from "react";
import Button from "@/app/components/Button";
import Table from "@/app/components/table"; 
import styles from '@/app/utils/css/dash/'


interface TableRowData {
  'INVOICE NO': string;
  'GRADE': string;
  'GARDEN': string;
  'NO OF BAGS': number;
  'PALLET WEIGHT': string; // Assuming these might include units like "kg"
  'TARE WEIGHT': string;
  'NET WEIGHT': string;
  'GROSS WEIGHT': string;
  'READ WEIGH WEIGHT': string; // Initially just a button
}
const handleReadWeight = (rowData: TableRowData) => {
    // This function will be called when the "Read" button is clicked
    console.log('Read button clicked for:', rowData);
    // Here you would implement the logic to get the "read weight" data
    // and potentially update the tableData state for this row.
    // For example:
    // fetch(`/api/read-weight/${rowData['INVOICE NO']}`)
    //   .then(response => response.json())
    //   .then(data => {
    //     const updatedData = tableData.map(row =>
    //       row['INVOICE NO'] === rowData['INVOICE NO'] ? { ...row, 'READ WEIGH WEIGHT': data.weight } : row
    //     );
    //     setTableData(updatedData);
    //   });
};
const columns = [
  { key: 'INVOICE NO', header: 'INVOICE NO' },
  { key: 'GRADE', header: 'GRADE' },
  { key: 'GARDEN', header: 'GARDEN' },
  { key: 'NO OF BAGS', header: 'NO OF BAGS' },
  { key: 'PALLET WEIGHT', header: 'PALLET WEIGHT' },
  { key: 'TARE WEIGHT', header: 'TARE WEIGHT' },
  { key: 'NET WEIGHT', header: 'NET WEIGHT' },
  { key: 'GROSS WEIGHT', header: 'GROSS WEIGHT' },
  {
    key: 'READ WEIGH WEIGHT',
    header: 'READ WEIGH WEIGHT',
    render: (item: TableRowData) => (
      <button className="read-button" onClick={() => handleReadWeight(item)}>
        Read
      </button>
    ),
  },
];

const MyReusableTable = () => {
  const [tableData, setTableData] = useState<TableRowData[]>([
    {
      'INVOICE NO': 'INV-001',
      'GRADE': 'BP1',
      'GARDEN': 'ABC Tea Garden',
      'NO OF BAGS': 100,
      'PALLET WEIGHT': '50 kg',
      'TARE WEIGHT': '5 kg',
      'NET WEIGHT': '45 kg',
      'GROSS WEIGHT': '55 kg',
      'READ WEIGH WEIGHT': '', // Initially empty, the button will be rendered
    },
    {
      'INVOICE NO': 'INV-002',
      'GRADE': 'PF1',
      'GARDEN': 'XYZ Tea Garden',
      'NO OF BAGS': 120,
      'PALLET WEIGHT': '60 kg',
      'TARE WEIGHT': '6 kg',
      'NET WEIGHT': '54 kg',
      'GROSS WEIGHT': '66 kg',
      'READ WEIGH WEIGHT': '', // Initially empty, the button will be rendered
    },
  ]);

  return (
    <div>
      <table>
        <tbody>
          <tr>
            <td colSpan={9} className="search-filter-row">
              <div className="search-filter-container">
                <div>
                  <label htmlFor="teaSearch" className="search-label">
                    Tea receiving
                  </label>
                  <div className="search-input-group">
                    <input
                      id="teaSearch"
                      defaultValue="Search by Consignment Number"
                      type="text"
                      className="search-input"
                    />
                    <Button type="button" className={styles['search-button']}>
                      Search
                    </Button>
                    <button type="button" id="printSummary" className="print-button">
                      Print Summary
                    </button>
                  </div>
                </div>
                <div>
                  <label htmlFor="invoiceFilter" className="search-label">
                    Filter by Invoice:
                  </label>
                  <input
                    type="text"
                    id="invoiceFilter"
                    placeholder="Invoice No."
                    className="filter-input"
                  />
                  <button type="search" className="search-button">
                    Search
                  </button>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <Table data={tableData} columns={columns} />
    </div>
  );
};

export default MyReusableTable;