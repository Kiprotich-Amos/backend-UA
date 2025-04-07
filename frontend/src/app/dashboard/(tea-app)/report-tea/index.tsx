"use client";
import React, { useState } from "react";
import styles from "@/app/utils/css/dash/report.module.css";

interface TableRowData {
  invoiceNo: string;
  grade: string;
  garden: string;
  noOfBags: number;
  palletWeight: string;
  tareWeight: string;
  netWeight: string;
  grossWeight: string;
  readWeight: string;
}

const ReceivingPage: React.FC = () => {
  const [tableData, setTableData] = useState<TableRowData[]>([
    {
      invoiceNo: "INV-001",
      grade: "BP1",
      garden: "ABC Tea Garden",
      noOfBags: 100,
      palletWeight: "50 kg",
      tareWeight: "5 kg",
      netWeight: "45 kg",
      grossWeight: "55 kg",
      readWeight: "",
    },
    {
      invoiceNo: "INV-002",
      grade: "PF1",
      garden: "XYZ Tea Garden",
      noOfBags: 120,
      palletWeight: "60 kg",
      tareWeight: "6 kg",
      netWeight: "54 kg",
      grossWeight: "66 kg",
      readWeight: "",
    },
  ]);

  const handleRead = (index: number) => {
    const updated = [...tableData];
    updated[index].readWeight = "Read: 47.5 kg";
    setTableData(updated);
  };

  return (
    <section className={styles.tableCard}>
      <div className={styles.searchFilterRow}>
        <div className={styles.searchFilterContainer}>
          <div>
            <label htmlFor="teaSearch" className={styles.searchLabel}>
              Tea Receiving
            </label>
            <div className={styles.searchInputGroup}>
              <input
                id="teaSearch"
                placeholder="Search by Consignment Number"
                type="text"
                className={styles.searchInput}
              />
              <button className={styles.searchButton}>Search</button>
              <button className={styles.printButton}>Print Summary</button>
            </div>
          </div>
          <div>
            <label htmlFor="invoiceFilter" className={styles.searchLabel}>
              Filter by Invoice:
            </label>
            <input
              type="text"
              id="invoiceFilter"
              placeholder="Invoice No."
              className={styles.filterInput}
            />
            <button className={styles.searchButton}>Search</button>
          </div>
        </div>
      </div>

      <table className={styles.table}>
        <thead>
          <tr>
            <th>INVOICE NO</th>
            <th>GRADE</th>
            <th>GARDEN</th>
            <th>NO OF BAGS</th>
            <th>PALLET WEIGHT</th>
            <th>TARE WEIGHT</th>
            <th>NET WEIGHT</th>
            <th>GROSS WEIGHT</th>
            <th>READ WEIGH WEIGHT</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((row, index) => (
            <tr key={row.invoiceNo}>
              <td>{row.invoiceNo}</td>
              <td>{row.grade}</td>
              <td>{row.garden}</td>
              <td>{row.noOfBags}</td>
              <td>{row.palletWeight}</td>
              <td>{row.tareWeight}</td>
              <td>{row.netWeight}</td>
              <td>{row.grossWeight}</td>
              <td>
                {row.readWeight ? (
                  row.readWeight
                ) : (
                  <button
                    className={styles.readButton}
                    onClick={() => handleRead(index)}
                  >
                    Read
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
};

export default ReceivingPage;
